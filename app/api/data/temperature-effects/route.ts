import { NextResponse } from "next/server"

// Optimized data with fewer points for better performance
const temperatureEffectsData = [
  { temperature: "30°C", ecoli: 65, yeast: 75 },
  { temperature: "37°C", ecoli: 90, yeast: 50 },
  { temperature: "40°C", ecoli: 45, yeast: 30 },
]

export async function GET() {
  return NextResponse.json(temperatureEffectsData)
}

