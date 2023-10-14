import { ReactNode, useEffect, useRef, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowRight } from '@fortawesome/free-solid-svg-icons'
import './App.css';

function Tile({ children }: {children?: ReactNode}) {
  return (
    <div className='bg-slate-200 rounded-xl w-full mb-4 p-2 shadow flex items-center justify-between'>
      {children}
    </div>
  );
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
  const genres = ['Waltz'];
  const keySigs = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
  const emotions = ['Happy', 'Sad']

  const [genreIndex, setGenreIndex] = useState(0);
  const [keySigIndex, setKeySigIndex] = useState(0);
  const [emotionIndex, setEmotionIndex] = useState(0);

  const [tempo, setTempo] = useState(60);
  const [chaosFactor, setChaosFactor] = useState(0);

  return (
    <div className='App'>
      <div className='w-full p-4 shadow-md flex items-center justify-between'>
        <h1 className='font-bold text-xl'>ostinato</h1>
        <div/>
      </div>
      <div className='flex flex-col md:flex-row w-3/5 m-auto'>
        <div className='flex-1 p-4 pr-2'>
          <Tile>
            <div>Genre</div>
            <Dropdown items={genres} onChange={index => setGenreIndex(index)} />
          </Tile>
          <Tile>
            <div>Tempo</div>
            <Slider min={60} max={180} step={1} onChange={value => setTempo(value)} />
          </Tile>
          <Tile>
            <div>Chaos factor</div>
            <Slider min={0} max={1} step={0.001} onChange={value => setChaosFactor(value)} />
          </Tile>
          <Tile>
            <div>Key signature</div>
            <Dropdown items={keySigs} onChange={index => setKeySigIndex(index)} />
          </Tile>
          <Tile>
            <div>Emotion</div>
            <Dropdown items={emotions} onChange={index => setEmotionIndex(index)} />
          </Tile>
          <div className='flex flex-row justify-between'>
            <div/>
            <button className='bg-green-300 rounded-full p-4'>
              Let's go
              <FontAwesomeIcon className='ml-2' icon={faArrowRight} />
            </button>
          </div>
          {/*<button onClick={() => alert(genres[genreIndex] + ' ' + keySigs[keySigIndex] + ' ' + tempo + ' ' + chaosFactor)}>show params</button>*/}
        </div>
        <div className='flex-1 p-4 pl-2'>
          <Tile>Output here</Tile>
        </div>
      </div>
    </div>
  );
}

export default App;
