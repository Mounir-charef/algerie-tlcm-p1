import {useEffect, useState} from 'react';
import axios from "axios";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "react-chartjs-2";

ChartJS.register(ArcElement, Tooltip, Legend);


const ChartPage = () => {
    const [data, setData] = useState(null)


    useEffect(() => {
            const getData = async () => {
            const result = await axios.get('http://127.0.0.1:8000/api/cmp/?month=1', {withCredentials: true});
            setData(
                {
                        labels: (result.data).map(info => info.cmp_name),
                        datasets: [
                            {
                                label: 'Binome',
                                data: result.data.map(info => info.binome),
                                backgroundColor: [
                                    'rgba(255, 99, 132, 0.7)',
                                    'rgba(54, 162, 235, 0.7)',
                                    'rgba(255, 206, 86, 0.7)',
                                    'rgba(75, 192, 192, 0.7)',
                                    'rgba(153, 102, 255, 0.7)',
                                    'rgba(255, 159, 64, 0.7)'
                                ],
                                borderColor: [
                                    'rgba(255, 99, 132, 1)',
                                    'rgba(54, 162, 235, 1)',
                                    'rgba(255, 206, 86, 1)',
                                    'rgba(75, 192, 192, 1)',
                                    'rgba(153, 102, 255, 1)',
                                    'rgba(255, 159, 64, 1)'
                                ],
                                borderWidth: 1,
                                hoverOffset: 4,
                            },
                        ],
                }
            )};

            const options = {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        position: 'right',
                    },
                    title: {
                        display: true,
                        text: 'Chart.js Doughnut Chart'
                    },
                }
            }

            getData().catch(err => console.table(err))
    }, [])
    if( !data) {
        return <p> loading </p>
    }
    return (
        <div style={{height: "70%", width: "70%", padding: 0, margin:0}}>
            <Doughnut data={data}
                      options={{
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: {
                                    position: 'right',
                                }
                            }
                        }}
            />
        </div>
    );
};

export default ChartPage;