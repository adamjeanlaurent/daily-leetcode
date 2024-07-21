/*
    Link: https://leetcode.com/problems/number-of-islands/description/

    Time Took: 23 minutes

    Time Complexity: O(M+N). Must visit every cell in the grid (at worst case twice)

    Space Complexity: O(1), only additonal space needed in the queue

    Solution Explained:

    - Do a BFS when land is found, find all adjacent land and when visited mark as water (as to not visit again.)
*/

const LAND: string = "1";
const WATER: string = "0";

class Cell {
    row: number;
    col: number;

    constructor(row: number, col: number) {
        this.row = row;
        this.col = col;
    }
}

function bfs(grid: string[][], startRow: number, startCol: number): void {
    let queue: Cell[] = [ new Cell(startRow, startCol) ];
    grid[startRow][startCol] = WATER; 

    while(queue.length > 0) {
        const cell: Cell = queue.shift()!;

        const neighbours: Cell[] = [
            new Cell(cell.row, cell.col - 1), // left
            new Cell(cell.row, cell.col + 1), // right
            new Cell(cell.row - 1, cell.col), // up
            new Cell(cell.row + 1, cell.col), // down
        ];

        for (const neighbour of neighbours) {
            if (neighbour.col >= 0 
                && neighbour.col < grid[0].length
                && neighbour.row >= 0 
                && neighbour.row < grid.length
                && grid[neighbour.row][neighbour.col] === LAND
            ) {
                grid[neighbour.row][neighbour.col] = WATER; 
                queue.push(neighbour);
            }
        }
    }
}

function numIslands(grid: string[][]): number {
    let numberOfIslands: number = 0;
    
    for(let row: number = 0; row < grid.length; row++) {
        for (let col: number = 0; col < grid[row].length; col++) {
            if (grid[row][col] === LAND) {
                bfs(grid, row, col);
                numberOfIslands++;
            }
        }
    }

    return numberOfIslands;
}