import { ReactNode, useEffect, useRef, useState } from 'react';
import { makeRequest } from './api';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowRight, faChevronDown, faChevronUp, faPause, faPlay } from '@fortawesome/free-solid-svg-icons';
import { Wave } from '@foobar404/wave';
import './App.css';

/*function getAudioStream(audio: HTMLAudioElement) {
  const audCtx = new AudioContext();
  const source = audCtx.createMediaElementSource(audio);
  const dest = audCtx.createMediaStreamDestination();
  source.connect(dest);
  return dest.stream;
}*/

function Tile({ className, children }: {className?: string, children?: ReactNode}) {
  return (
    <div className={'bg-slate-200 dark:bg-slate-900 rounded-xl w-full mb-4 p-2 shadow flex items-center justify-between ' + (className || '')}>
      {children}
    </div>
  );
}

function DropdownTile({ label, items, onChange }: {label: string, items: string[], onChange?: (index: number) => void}) {
  const [expanded, setExpanded] = useState(false);
  const [index, setIndex] = useState(0);

  function onItemClick(index: number) {
    setIndex(index);
    //setExpanded(false);
  }

  return (
    <div className='bg-slate-200 dark:bg-slate-900 rounded-xl w-full mb-4 p-2 shadow flex flex-col' onClick={() => setExpanded(!expanded)}>
      <div className='flex items-center justify-between'>
        <div className='font-bold'>{label}</div>
        <div className='flex items-center'>
          <div>{items[index]}</div>
          <FontAwesomeIcon icon={expanded ? faChevronUp : faChevronDown} className='pl-2' />
        </div>
      </div>
      <div className={'flex flex-col ' + (expanded ? '' : 'hidden')}>
        {items.map((item, index) => <button className='text-left bg-slate-100 dark:bg-slate-800 rounded mt-1 p-1' onClick={() => onItemClick(index)}>{item}</button>)}
      </div>
    </div>
  )
}

function Dropdown({ items, onChange }: {items: string[], onChange?: (index: number) => void}) {
  const [expanded, setExpanded] = useState(false);
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (onChange) {
      onChange(index);
    }
  }, [index]);

  function onItemClick(index: number) {
    setIndex(index);
    setExpanded(false);
  }

  return (
    <div className='flex flex-col'>
      <button className='bg-white rounded p-2' onClick={() => setExpanded(!expanded)}>{items[index]}</button>
      <div className={'flex flex-col ' + (expanded ? '' : 'hidden')}>
        {items.map((item, index) => <button className='bg-slate-100 rounded mt-1 p-1' onClick={() => onItemClick(index)}>{item}</button>)}
      </div>
    </div>
  );
}

function Slider({ className, min, max, step, onChange }: {className?: string, min: number, max: number, step: number, onChange?: (value: number) => void}) {
  const rangeInput = useRef<HTMLInputElement>(null);

  return (
    <div className={'-mt-1 mr-2 ' + (className || '')}>
      <input ref={rangeInput} className='appearance-none w-full h-1 bg-gray-300 outline-none rounded [&::-moz-range-thumb]:bg-blue-600 [&::-moz-range-thumb]:rounded-full' type='range' min={min} max={max} step={step} onChange={() => {
        if (onChange) {
          onChange(rangeInput.current ? parseFloat(rangeInput.current.value) : min);
        }
      }} />
    </div>
  );
}

function App() {
  const genres = ['Waltz', 'Hello', 'World'];
  const keySigs = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
  const emotions = ['Happy', 'Sad']

  const [genreIndex, setGenreIndex] = useState(0);
  const [keySigIndex, setKeySigIndex] = useState(0);
  const [emotionIndex, setEmotionIndex] = useState(0);

  const [tempo, setTempo] = useState(60);
  const [chaosFactor, setChaosFactor] = useState(0);

  const [audio, setAudio] = useState<HTMLAudioElement | null>(null);
  const [playing, setPlaying] = useState(false);

  const visualizerCanvas = useRef<HTMLCanvasElement>(null);

  const toggle: () => void = () => setPlaying(!playing);

  useEffect(() => {
    if (audio) {
      audio.addEventListener('ended', () => setPlaying(false));
      setPlaying(true);
    } else {
      setPlaying(false);
    }
  }, [audio])

  useEffect(() => {
      audio && (playing ? audio.play() : audio.pause());
    },
    [playing]
  );

  /*useEffect(() => {
    audio.addEventListener('ended', () => setPlaying(false));
    return () => {
      audio.removeEventListener('ended', () => setPlaying(false));
    };
  }, []);*/

  useEffect(() => {
    if (audio && visualizerCanvas.current) {
      const dark = window.matchMedia("(prefers-color-scheme: dark)").matches;
      const wave = new Wave(audio, visualizerCanvas.current);
      wave.addAnimation(new wave.animations.Wave({ fillColor: dark ? '#fff' : '#000', lineColor: dark ? '#fff' : '#000' }));
    }
  }, [audio])

  function onLetsGoClicked() {
    makeRequest({
      tempo: tempo,
      genre: genres[genreIndex],
      key_signature: keySigs[keySigIndex],
      chaos_factor: chaosFactor,
      emotion: emotions[emotionIndex]
    }).then(json => {
      const audio = new Audio(json.path);
      audio.crossOrigin = 'anonymous';
      audio.loop = true;
      setAudio(audio);
    })
  }

  return (
    <div className='App h-full dark:text-white'>
      <div className='w-full p-4 flex items-center justify-between'>
        <h1 className='font-bold text-xl'>ostinato</h1>
        <div/>
      </div>
      <div className='flex flex-col-reverse md:flex-row w-full md:w-3/5 m-auto'>
        <div className='flex-1 p-4 md:pr-2'>
          {/*<Tile>
            <div>Genre</div>
            <Dropdown items={genres} onChange={index => setGenreIndex(index)} />
          </Tile>*/}
          <DropdownTile label='Genre' items={genres} onChange={index => setGenreIndex(index)} />
          <Tile>
            <div className='font-bold flex-1'>Tempo</div>
            <div className='flex-1 flex'>
              <Slider className='flex-1' min={60} max={180} step={1} onChange={value => setTempo(value)} />
              <div className='w-12 text-center'>{tempo}</div>
            </div>
          </Tile>
          <Tile>
            <div className='font-bold flex-1'>Chaos factor</div>
            <div className='flex-1 flex'>
              <Slider className='flex-1' min={0} max={1} step={0.001} onChange={value => setChaosFactor(value)} />
              <div className='w-12 text-center'>{chaosFactor}</div>
            </div>
          </Tile>
          <DropdownTile label='Key signature' items={keySigs} onChange={index => setKeySigIndex(index)} />
          <DropdownTile label='Emotion' items={emotions} onChange={index => setEmotionIndex(index)} />
          <div className='flex flex-row justify-between'>
            <div/>
            <button className='bg-green-300 text-black rounded-full p-4 mt-4 w-full md:w-auto' onClick={onLetsGoClicked}>
              Let's go
              <FontAwesomeIcon className='ml-2' icon={faArrowRight} />
            </button>
          </div>
          {/*<button onClick={() => alert(genres[genreIndex] + ' ' + keySigs[keySigIndex] + ' ' + tempo + ' ' + chaosFactor)}>show params</button>*/}
        </div>
        <div className='flex-1 p-4 pb-0 md:pl-2'>
          <Tile className='flex-col mb-0'>
            <canvas ref={visualizerCanvas} className='w-full rounded m-2'></canvas>
            <div>
              <div/>
              <button className='w-12 h-12 bg-pink-500 rounded-full' onClick={toggle as () => void}>
                <FontAwesomeIcon icon={playing ? faPause : faPlay} />
              </button>
              <div/>
            </div>
          </Tile>
        </div>
      </div>
    </div>
  );
}

export default App;