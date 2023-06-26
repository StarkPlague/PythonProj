import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.PriorityQueue;

public class GhokemonMain {
	public static void main(String[] args) throws IOException {

		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

		WorldObject worldObjects = new WorldObject();
		Logy logy = new Logy();
		WorldMaze worldMaze = new WorldMaze();

		logy.setWorldObjects(worldObjects);
		logy.setWorldMaze(worldMaze);

		String input = in.readLine();

		int row = Integer.parseInt(input.split(" ")[0]);
		int column = Integer.parseInt(input.split(" ")[1]);

		int ghokemonAmount = Integer.parseInt(input.split(" ")[2]);
		int enemyAmount = Integer.parseInt(input.split(" ")[3]);
		int maxGhokemon = Integer.parseInt(input.split(" ")[4]);

		logy.setMaxGhoke(maxGhokemon);

		char[][] maze = new char[row][column];

		// creating the field, adding ascii char to array. also detecting Logy,
		// also detecting logy position

		String fieldPerRow;
		int logyColumn = 0, logyRow = 0;

		for (int i = 0; i < row; i++) {
			fieldPerRow = in.readLine();
			for (int j = 0; j < column; j++) {
				char temp = fieldPerRow.charAt(j);
				maze[i][j] = temp;

				if (temp == 'L') {
					logyColumn = j;
					logyRow = i;
				}

			}
		}

		//System.out.println(logyRow + ", " + logyColumn);

		Point logyPosition = new Point(logyRow, logyColumn); //
		logy.setPosition(logyPosition); // set posisi logy
		worldMaze.setMaze(maze); // masukkin maze ke world maze

		// creating new ghokemon from user input and add them to world objects

		String addGhokemon;
		Ghokemon newGhokemon;
		while (ghokemonAmount > 0) {
			ArrayList<Ghokemon> arrOfGhokemon = new ArrayList<Ghokemon>();
			addGhokemon = in.readLine();
			int ghokemonRow = Integer.parseInt(addGhokemon.split(" ")[0])-1;
			int ghokemonColumn = Integer.parseInt(addGhokemon.split(" ")[1])-1;
			String ghokemonName = addGhokemon.split(" ")[2];
			char ghokemonType = addGhokemon.split(" ")[3].charAt(0);
			int ghokemonStamina = Integer.parseInt(addGhokemon.split(" ")[4]);

			newGhokemon = new Ghokemon(ghokemonRow, ghokemonColumn, ghokemonName, ghokemonType, ghokemonStamina);
			Point coordinates = new Point(ghokemonRow, ghokemonColumn);

			// adding ghokemon to arraylist of ghokemon in worldobjects
			// if not available, add arraylist to the wolrld objects hashmap

			if (worldObjects.getGhokemonList().containsKey(coordinates)) {
				worldObjects.getGhokemonList().get(coordinates).add(newGhokemon);
				//System.out.println("ghokemon in petak already exist");
			} else {
				arrOfGhokemon.add(newGhokemon);
				worldObjects.getGhokemonList().put(coordinates, arrOfGhokemon);
				//System.out.println("ghokemon added");
			}

			ghokemonAmount--;
		}
		
		// add trainer and trainer's ghokemon

		String addGhokemonEnemy;

		while (enemyAmount > 0) {
			addGhokemonEnemy = in.readLine();

			int ghokemonEnemyRow = Integer.parseInt(addGhokemonEnemy.split(" ")[0]);
			int ghokemonEnemyColumn = Integer.parseInt(addGhokemonEnemy.split(" ")[1]);
			char ghokemonType = addGhokemonEnemy.split(" ")[2].charAt(0);

			Ghokemon newGhokemonEnemy = new Ghokemon(ghokemonEnemyRow, ghokemonEnemyColumn, ghokemonType);

			Enemy enemyTemp = new Enemy(ghokemonEnemyRow, ghokemonEnemyColumn);

			// nambahin ghokemonnya di trainer
			enemyTemp.getGhokemonList().add(newGhokemonEnemy);
			Point temp = new Point(ghokemonEnemyRow, ghokemonEnemyColumn);

			// nambahin trainer nya di dalam worldobjects
			worldObjects.getTrainerList().put(temp, enemyTemp);

			enemyAmount--;
		}

		logy.run(logy.getPosition());

	}
}

// class untuk menyimpan semua object (trainer dan ghokemon) di map
class WorldObject {

	private HashMap<Point, Enemy> trainerList;
	private HashMap<Point, ArrayList<Ghokemon>> ghokemonList;
	private char[][] worldField;

	public WorldObject() {
		trainerList = new HashMap<Point, Enemy>();
		ghokemonList = new HashMap<Point, ArrayList<Ghokemon>>();
	}

	public HashMap<Point, Enemy> getTrainerList() {
		return this.trainerList;
	}

	// get arrayList of ghokemon at specified coordinates
	public HashMap<Point, ArrayList<Ghokemon>> getGhokemonList() {
		return this.ghokemonList;
	}
}

// class untuk map raw nya, cuman containing arr of char dan lain2 yang primitif

class WorldMaze {

	char[][] worldMaze;
	private int maxRow, maxColumn;

	public WorldMaze() {

	}

	public void setMaze(char[][] m) {
		this.worldMaze = m;
		this.maxRow = m.length;
		this.maxColumn = m[0].length;
	}

	public int getMaxRow() {
		return this.maxRow;
	}

	public int getMaxColumn() {
		return this.maxColumn;
	}

	public char[][] getWorldMaze() {
		return this.worldMaze;
	}
}

class Logy {

	private Point position;
	private int maxGhokemon;
	private boolean isClockwise;
	private GhokemonCollection logyGhoke;
	private WorldObject worldObjects;
	private WorldMaze worldMaze;

	public Logy() {
		isClockwise = true;
		logyGhoke = new GhokemonCollection();
	}

	public void setPosition(Point p) {
		this.position = p;
	}

	public Point getPosition() {
		return this.position;
	}

	public void setMaxGhoke(int max) {
		this.maxGhokemon = max;
	}

	public void setWorldObjects(WorldObject obj) {
		this.worldObjects = obj;
	}

	public void setWorldMaze(WorldMaze m) {
		this.worldMaze = m;
	}

	public GhokemonCollection getGhokemonCollection() {
		return this.logyGhoke;
	}

	public int getMaxGhokemon() {
		return this.maxGhokemon;
	}

	public void run(Point p) {

		if (!isValidPoint(p)) {
			return;
		}

		// System.out.println("Posisi: " + p.getRow() + ", " + p.getColumn());
		if (worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] == 'T') {
			worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] = '#';
			battle(p);
			//System.out.printf(" at (%d , %d) %n", p.getRow(), p.getColumn());
		}

		if (worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] == 'G') {
			worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] = '#';
			follow(p);
			//System.out.printf(" at (%d , %d) %n", p.getRow(), p.getColumn());
		}

		if (worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] == '?') {
			worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] = '#';
			toggleOrientation();
			//System.out.printf(" at (%d , %d) %n", p.getRow(), p.getColumn());
		}

		worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] = '#';

		/*run(p.headNorth());
		run(p.headEast());
		run(p.headSouth());
		run(p.headWest());*/
		
		if (isClockwise) {
			run(p.headNorth());

			if (isClockwise) {
				run(p.headEast());
			} else {
				run(p.headWest());
			}
			run(p.headSouth());
			if (isClockwise) {
				run(p.headEast());
			} else {
				run(p.headWest());
			}
		} else {
			run(p.headNorth());
			if (isClockwise) {
				run(p.headEast());
			} else {
				run(p.headWest());
			}
			run(p.headSouth());
			if (isClockwise) {
				run(p.headEast());
			} else {
				run(p.headWest());
			}
		}

		/*
		 * run(p.headNorth()); if(isClockwise){ run(p.headWest()); } else {
		 * run(p.headEast()); } run(p.headSouth()); if (isClockwise) {
		 * run(p.headEast()); } else { run(p.headWest()); }
		 */

	}

	public void battle(Point p) {
		
		//Ghokemon ghokemonPetarung = null;
		
		if(logyGhoke.getGhokemonCount() == 0){
			System.out.printf("NO BATTLE %d %d %n", p.getRow()+1, p.getColumn()+1);
			return;
		}
		
		if(this.worldObjects.getTrainerList().size() == 0){
			System.out.println("no trainer");
			return;
		}
		
		System.out.println(this.worldObjects.getTrainerList().size());
		System.out.println(this.worldObjects.getTrainerList().get(p).getType());
		
		char trainerType = ' ';
		
		// kalo api
		if(trainerType == 'F'){
			
			// cari yang air dulu
			if(logyGhoke.getWaterGhokemonList().size() != 0){
				logyGhoke.getWaterGhokemonList().poll();
			} else {
				// kalo gaada cari yang api
				if(logyGhoke.getFireGhokemonList().size()!=0){
					logyGhoke.getFireGhokemonList().poll();
				} else {
					//terakhir, ambil yang rumput
					logyGhoke.getGrassGhokemonList().poll();
				}
			}
			
		} else if (trainerType == 'G'){
			// cari yang api dulu
			if (logyGhoke.getFireGhokemonList().size() != 0) {
				logyGhoke.getFireGhokemonList().poll();
			} else {
				// kalo gaada cari yang rumput
				if (logyGhoke.getGrassGhokemonList().size() != 0) {
					logyGhoke.getFireGhokemonList().poll();
				} else {
					// terakhir, ambil yang air
					logyGhoke.getWaterGhokemonList().poll();
				}
			}
			
		} else {
			// cari yang rumput dulu
			if (logyGhoke.getGrassGhokemonList().size() != 0) {
				logyGhoke.getGrassGhokemonList().poll();
			} else {
				// kalo gaada cari yang air
				if (logyGhoke.getWaterGhokemonList().size() != 0) {
					logyGhoke.getWaterGhokemonList().poll();
				} else {
					// terakhir, ambil yang api
					logyGhoke.getFireGhokemonList().poll();
				}
			}
		}
		
	}

	public void follow(Point p) {

		ArrayList<Ghokemon> ghokeDiPetak = this.worldObjects.getGhokemonList().get(p);
		
		// ini buat ngecek aja
		/*System.out.printf("posisi: row %d column %d ada ", p.getRow(), p.getColumn());
		if(ghokeDiPetak != null){
			System.out.println(ghokeDiPetak.size() + " ghokemon");
		} else {
			System.out.println("null");
		}*/
			
		/*for(Ghokemon ghoke : ghokeDiPetak){
			System.out.print(ghoke.getName() +", ");
		}*/
		
		ArrayList<Ghokemon> addedGhoke = addGhoke(ghokeDiPetak);
		
		if(addedGhoke.size() == 0){
			System.out.print("ALL STAY");
			System.out.printf(" %d %d", p.getRow()+1, p.getColumn()+1);
		} else {
			System.out.printf("Follow %d %d: ", p.getRow()+1, p.getColumn()+1);

			for (int i = 0; i < addedGhoke.size(); i++) {
				System.out.print(addedGhoke.get(i).getName());
				if (i < addedGhoke.size() - 1) {
					System.out.print(", ");
				}
			}
		}
		
	
		
		System.out.println("");
	}

	public ArrayList<Ghokemon> addGhoke(ArrayList<Ghokemon> ghokeDiPetak) {
		
		ArrayList<Ghokemon> addedGhokemon = new ArrayList<Ghokemon>();
		PriorityQueue<Ghokemon> nominasiDibuang;
		Ghokemon terbuang = null;

		for (Ghokemon element : ghokeDiPetak) {

			if (element.getType() == 'F') {
				logyGhoke.getFireGhokemonList().offer(element);
			}

			if (element.getType() == 'G') {
				logyGhoke.getGrassGhokemonList().offer(element);
			}

			if (element.getType() == 'W') {
				logyGhoke.getWaterGhokemonList().offer(element);
			}

			if (logyGhoke.getGhokemonCount() > maxGhokemon) {
				
				//System.out.println("ada yang mau dibuang");

				nominasiDibuang = new PriorityQueue<Ghokemon>();
				int ghokeFireCount = logyGhoke.getFireGhokemonList().size();
				int ghokeWaterCount = logyGhoke.getWaterGhokemonList().size();
				int ghokeGrassCount = logyGhoke.getGrassGhokemonList().size();
				// jika jumlah list tiap tipe tidak 0, ambil terlemah tiap tipe
				if(ghokeFireCount != 0){
					nominasiDibuang.offer(logyGhoke.getFireGhokemonList().peek());
				}
				if(ghokeWaterCount != 0){
					nominasiDibuang.offer(logyGhoke.getWaterGhokemonList().peek());
				}
				if(ghokeGrassCount != 0){
					nominasiDibuang.offer(logyGhoke.getGrassGhokemonList().peek());
				}

				// ambil yang paling terlemah dari nominasi terbuang
				terbuang = nominasiDibuang.poll();

				// cektipe nya, poll dari queue tipe yang sesuai
				if (terbuang.getType() == 'F') {
					logyGhoke.getFireGhokemonList().poll();
				}

				if (terbuang.getType() == 'G') {
					logyGhoke.getGrassGhokemonList().poll();
				}

				if (terbuang.getType() == 'W') {
					logyGhoke.getWaterGhokemonList().poll();
				}
			}
			
			//System.out.println(element.getName() +" yey");
			
			// kalo yang terbuang bukan ghokemon yang lagi di add, masukkin
			// ghokemon itu ke addedGhokemon
			if(terbuang != null){
				if (!(terbuang.equals(element))){
					addedGhokemon.add(element);
				} else {
					System.out.println("\t" + terbuang.getName() + " dibuang");
				}
			} else{
				addedGhokemon.add(element);
			}
			/*if (!(terbuang.equals(element)) && terbuang != null) {
				addedGhokemon.add(element);
			}*/
		}

		return addedGhokemon;

	}

	public void toggleOrientation() {
		isClockwise = !isClockwise;
		//System.out.print("\t change orientation");
	}

	public boolean isValidPoint(Point p) {
		return (p.getRow() < worldMaze.getMaxRow() && p.getColumn() < worldMaze.getMaxColumn() && p.getRow() >= 0
				&& p.getColumn() >= 0 && worldMaze.getWorldMaze()[p.getRow()][p.getColumn()] != '#');
	}
}

class GhokemonCollection {

	private PriorityQueue<Ghokemon> grassGhokemon;
	private PriorityQueue<Ghokemon> fireGhokemon;
	private PriorityQueue<Ghokemon> waterGhokemon;

	public GhokemonCollection() {
		this.grassGhokemon = new PriorityQueue<Ghokemon>();
		this.fireGhokemon = new PriorityQueue<Ghokemon>();
		this.waterGhokemon = new PriorityQueue<Ghokemon>();
	}

	public PriorityQueue<Ghokemon> getGrassGhokemonList() {
		return this.grassGhokemon;
	}

	public PriorityQueue<Ghokemon> getFireGhokemonList() {
		return this.fireGhokemon;
	}

	public PriorityQueue<Ghokemon> getWaterGhokemonList() {
		return this.waterGhokemon;
	}

	public int getGhokemonCount() {
		return (grassGhokemon.size() + fireGhokemon.size() + waterGhokemon.size());
	}
}

class Ghokemon implements Comparable<Ghokemon> {
	private int row;
	private int column;
	private String name;
	private char type;
	private int stamina;
	private int duration;

	public Ghokemon(int row, int column, String name, char type, int stamina) {
		this.row = row;
		this.column = column;
		this.name = name;
		this.type = type;
		this.stamina = stamina;
	}

	public Ghokemon(int row, int column, char type) {
		this.row = row;
		this.column = column;
		this.type = type;
	}

	public int getRow() {
		return this.row;
	}

	public int getColumn() {
		return this.column;
	}

	public int getStamina() {
		return this.stamina;
	}

	public char getType() {
		return this.type;
	}

	public int getDuration() {
		return this.duration;
	}

	public String getName() {
		return this.name;
	}

	// compare untuk mengluarkan pokemmon pas battle
	public int compareTo(Ghokemon other) {

		if (this.getStamina() == other.getStamina()) {
			return other.getDuration() - getDuration();
		} else {
			return getStamina() - other.getStamina();
		}
	}

	public boolean equals(Ghokemon other) {
		return name.equals(other.getName());
	}
}

class Enemy {

	private int row;
	private int column;
	private ArrayList<Ghokemon> ghokemonList;
	private char type;
	
	public Enemy(int row, int column) {
		this.row = row;
		this.column = column;
		ghokemonList = new ArrayList<Ghokemon>();
	}

	public int getRow() {
		return this.row;
	}

	public int getColumn() {
		return this.column;
	}

	public Ghokemon launchGhokemon() {
		return this.ghokemonList.get(0);
	}

	public ArrayList<Ghokemon> getGhokemonList() {
		return this.ghokemonList;
	}
	
	public char getType(){
		type = ghokemonList.get(0).getType();
		return this.type;
	}
	
	public void addGhokemon(Ghokemon ghoke){
		ghokemonList.add(ghoke);
	}
}

class Point {

	private int row;
	private int column;

	public Point(int row, int column) {
		this.row = row;
		this.column = column;
	}

	public int getRow() {
		return this.row;
	}

	public int getColumn() {
		return this.column;
	}

	public Point headNorth() {
		return new Point(row - 1, column);
	}

	public Point headSouth() {
		return new Point(row + 1, column);
	}

	public Point headWest() {
		return new Point(row, column - 1);
	}

	public Point headEast() {
		return new Point(row, column + 1);
	}

	@Override
	public int hashCode() {
		// hashcode based on intelliJ automatic hashcode generation procedure.
		int result = column;
		result = 2501 * result + row;
		return result;

	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see java.lang.Object#equals(java.lang.Object)
	 */
	@Override
	public boolean equals(Object obj) {
		// TODO Auto-generated method stub
		return this.getRow() == ((Point) obj).getRow() && this.getColumn() == ((Point) obj).getColumn();
	}
}