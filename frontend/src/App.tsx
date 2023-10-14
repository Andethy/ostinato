import React, { ReactNode } from 'react';
import logo from './logo.svg';
import './App.css';

function Tile({ children }: {children?: ReactNode}) {
  return (
    <div className='bg-slate-200 rounded-xl w-full mb-4 p-2 shadow flex justify-between'>
      {children}
    </div>
  );
}

function App() {
  return (
    <div className='App'>
      <div className='w-full p-4 shadow-md flex items-center justify-between'>
        <h1 className='font-bold text-xl'>ostinato</h1>
        <div/>
      </div>
      <div className='flex flex-col md:flex-row w-3/5 m-auto'>
        <div className='flex-1 p-4 pr-2'>
          <Tile>Genre</Tile>
          <Tile>Tempo</Tile>
          <Tile>Chaos factor</Tile>
          <Tile>Key signature</Tile>
        </div>
        <div className='flex-1 p-4 pl-2'>
          <Tile>Output here</Tile>
        </div>
      </div>
    </div>
  );
}

export default App;
