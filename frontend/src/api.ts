type OstinatoRequest = {
  tempo: number,
  genre: string, //'waltz',
  chaos_factor: number,
  key_signature: string, //'C' | 'C#' | 'D' | 'D#' | 'E' | 'F' | 'F#' | 'G' | 'G#' | 'A' | 'A#' | 'B',
  emotion: string // 'happy'
}

export async function makeRequest(body: OstinatoRequest) {
  const response = await fetch('http://localhost:5000/ostinato_home', {
    method: 'POST',
    headers: {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
      //'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    },
    body: new URLSearchParams({
      'tempo': body.tempo.toString(),
      'genre': body.genre,
      'chaos_factor': body.chaos_factor.toString(),
      'key_signature': body.key_signature,
      'emotion': body.emotion
    })
  }); /*fetch('http://localhost:5000/ostinato_home', {
    headers: {},
    method: 'POST',
    body: JSON.stringify(body)
  });*/
  const json = await response.json();
  return json;
}