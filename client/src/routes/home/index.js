import { h } from 'preact';
import { useState, useEffect } from "preact/hooks";
import style from './style.css';

const Home = () => {
	const [data, setData] = useState(null);

	useEffect(() => {
		const fetchData = async () => {
			const result = await fetch('http://0.0.0.0:5000/game');
			const d = await result.text()
			setData(d)
		}

		fetchData();
	}, [])

	return (
		<div class={style.home}>
			<h1> {JSON.stringify(data)} </h1>
		</div>
	);
};

export default Home;
