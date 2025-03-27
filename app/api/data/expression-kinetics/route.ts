import { NextResponse } from "next/server"

// Optimized data with fewer points for better performance
const expressionKineticsData = [
  { time: 0, ecoli: 0, yeast: 0 },
  { time: 8, ecoli: 30, yeast: 12 },
  { time: 16, ecoli: 60, yeast: 30 },
  { time: 24, ecoli: 80, yeast: 50 },
  { time: 32, ecoli: 76, yeast: 60 },
  { time: 40, ecoli: 72, yeast: 63 },
  { time: 48, ecoli: 68, yeast: 58 },
]

export async function GET() {
  return NextResponse.json(expressionKineticsData)
}

