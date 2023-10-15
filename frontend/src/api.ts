type OstinatoRequest = {
  tempo: number,
  genre: string, //'waltz',
  chaos_factor: number,
  key_signature: string //'C' | 'C#' | 'D' | 'D#' | 'E' | 'F' | 'F#' | 'G' | 'G#' | 'A' | 'A#' | 'B'
}

export async function makeRequest(body: OstinatoRequest) {
  const response = await fetch('http://localhost:5000/ostinato_home', {
    headers: {},
    method: 'POST',
    body: JSON.stringify(body)
  });
  const json = await response.json();
  return json;
}