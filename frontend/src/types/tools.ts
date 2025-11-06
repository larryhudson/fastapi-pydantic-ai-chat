/**
 * Auto-generated types from backend tool schemas
 * Do not edit manually - run "npm run generate:types" to update
 */

export type City = string;
export type Condition = string;
export type Temperature = number;
export type Unit = string;

/**
 * Weather data model.
 */
export interface Weather {
  city: City;
  condition: Condition;
  temperature: Temperature;
  unit?: Unit;
  [k: string]: unknown;
}


// Tool output type mapping
export type ToolOutputTypes = {
  get_weather: Weather;
};
