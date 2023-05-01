import { h } from 'preact';
import { useState, useEffect } from "preact/hooks";
import Board from './board';
import { movePiece } from '../api';

const Game = () => {
    const [data, setData] = useState(null);
    const [to, setTo] = useState('');
    const [from, setFrom] = useState('')

    useEffect(() => {
        const fetchData = async () => {
            const result = await fetch('http://0.0.0.0:5000/game');
            const d = await result.text()
            setData(JSON.parse(d))
        }

        fetchData();
    }, [])

    const youGotToMoveItMoveIt = async (from, to) => {
        const newBoard = await movePiece(from, to);
        setData(newBoard)
    }


    if (!data) return 'Chill out dude its loading'

    return (
        <>
            <Board board={data.board} />
            <input value={to} onChange={(e) => setTo(e.target.value)}> to: </input>
            <input value={from} onChange={(e) => setFrom(e.target.value)}> From: </input>
            <button onClick={() => youGotToMoveItMoveIt(to, from)}> MOVE IT </button>
            <p> TURN: {data.white_turn ? "white" : "black"}</p>
        </>
    );
};

export default Game;
