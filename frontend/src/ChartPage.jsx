import {useEffect, useState} from 'react';
import axios from "axios";

const ChartPage = () => {
    const [data, setData] = useState(null)


    useEffect(() => {
            const getData = async () => {
            const result = await axios.get('http://127.0.0.1:8000/api/cmps/?month=1', {withCredentials: true});
            setData(result.data)
        };
            getData().catch(err => console.table(err))
    }, [])
    if( !data) {
        return <p> loading </p>
    }
    return (
        <div>
            {data.map(info => <p key={info.id}> {info.binome}</p> )}
        </div>
    );
};

export default ChartPage;