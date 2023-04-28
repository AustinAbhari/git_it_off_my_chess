import { h } from 'preact';
import { useState, useEffect } from "preact/hooks";
import Board from './board';

const Game = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            const result = await fetch('http://0.0.0.0:5000/game');
            const d = await result.text()
            setData(JSON.parse(d))
        }

        fetchData();
    }, [])

    if (!data) return 'Chill out dude its loading'

    return (
        <Board board={data.board} />
    );
};

export default Game;
