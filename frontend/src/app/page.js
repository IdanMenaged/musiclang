import Image from "next/image";
import Head from "next/head";

import logo from '../../res/logo.png'

export default function Home() {
  return (
    <>
      <main
        className="flex flex-col items-center justify-center h-screen"
      >
        <Image
        src={logo}
        width={180}
      />
        <h1
          className="m-8 text-3xl"
        >Welcome to Musiclang</h1>

        <form
          className="grid grid-cols-2 gap-4"
        >
          <div
            className="flex flex-col space-y-4 items-center"
          >
            <label htmlFor="playlist">Link to Playlist</label>
            <label htmlFor="language">Language</label>
          </div>
          <div
            className="flex flex-col space-y-4 items-center"
          >
            <input 
              id="playlist"
              className="border border-black"
            />
            <input 
              // make a select option
              id="language"
              className="border border-black"
            />
          </div>
        </form>
      </main>
    </>
  );
}
