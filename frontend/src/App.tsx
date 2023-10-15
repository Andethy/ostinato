import { ReactNode, useEffect, useRef, useState } from 'react';
import { makeRequest } from './api';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowRight, faChevronDown, faChevronUp, faPause, faPlay } from '@fortawesome/free-solid-svg-icons';
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
    <div className={'bg-slate-200 rounded-xl w-full mb-4 p-2 shadow flex items-center justify-between ' + (className || '')}>
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
    <div className='bg-slate-200 rounded-xl w-full mb-4 p-2 shadow flex flex-col' onClick={() => setExpanded(!expanded)}>
      <div className='flex items-center justify-between'>
        <div className='font-bold'>{label}</div>
        <div className='flex items-center'>
          <div>{items[index]}</div>
          <FontAwesomeIcon icon={expanded ? faChevronUp : faChevronDown} className='pl-2' />
        </div>
      </div>
      <div className={'flex flex-col ' + (expanded ? '' : 'hidden')}>
        {items.map((item, index) => <button className='text-left bg-slate-100 rounded mt-1 p-1' onClick={() => onItemClick(index)}>{item}</button>)}
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

function Slider({ min, max, step, onChange }: {min: number, max: number, step: number, onChange?: (value: number) => void}) {
  const rangeInput = useRef<HTMLInputElement>(null);

  return (
    <div className='-mt-2'>
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

  const [audio, setAudio] = useState(new Audio('https://github.com/prof3ssorSt3v3/media-sample-files/raw/master/fight-club.mp3'));
  const [playing, setPlaying] = useState(false);

  const toggle: () => void = () => setPlaying(!playing);

  useEffect(() => {
      playing ? audio.play() : audio.pause();
    },
    [playing]
  );

  useEffect(() => {
    audio.addEventListener('ended', () => setPlaying(false));
    return () => {
      audio.removeEventListener('ended', () => setPlaying(false));
    };
  }, []);

  function onLetsGoClicked() {
    makeRequest({
      tempo: tempo,
      genre: genres[genreIndex],
      key_signature: keySigs[keySigIndex],
      chaos_factor: chaosFactor,
      emotion: emotions[emotionIndex]
    });
  }

  return (
    <div className='App'>
      <div className='w-full p-4 shadow-md flex items-center justify-between'>
        <h1 className='font-bold text-xl'>ostinato</h1>
        <div/>
      </div>
      <div className='flex flex-col md:flex-row w-3/5 m-auto'>
        <div className='flex-1 p-4 pr-2'>
          {/*<Tile>
            <div>Genre</div>
            <Dropdown items={genres} onChange={index => setGenreIndex(index)} />
          </Tile>*/}
          <DropdownTile label='Genre' items={genres} onChange={index => setGenreIndex(index)} />
          <Tile>
            <div className='font-bold'>Tempo</div>
            <Slider min={60} max={180} step={1} onChange={value => setTempo(value)} />
          </Tile>
          <Tile>
            <div className='font-bold'>Chaos factor</div>
            <Slider min={0} max={1} step={0.001} onChange={value => setChaosFactor(value)} />
          </Tile>
          <DropdownTile label='Key signature' items={keySigs} onChange={index => setKeySigIndex(index)} />
          <DropdownTile label='Emotion' items={emotions} onChange={index => setEmotionIndex(index)} />
          <div className='flex flex-row justify-between'>
            <div/>
            <button className='bg-green-300 rounded-full p-4' onClick={onLetsGoClicked}>
              Let's go
              <FontAwesomeIcon className='ml-2' icon={faArrowRight} />
            </button>
          </div>
          {/*<button onClick={() => alert(genres[genreIndex] + ' ' + keySigs[keySigIndex] + ' ' + tempo + ' ' + chaosFactor)}>show params</button>*/}
        </div>
        <div className='flex-1 p-4 pl-2'>
          <Tile className='flex-col'>
            {/*recorder && <LiveAudioVisualizer mediaRecorder={recorder} />*/}
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