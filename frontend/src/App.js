import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { 
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, 
  ResponsiveContainer, ReferenceLine, Legend 
} from 'recharts';
import { Activity, AlertCircle, Calendar, TrendingDown } from 'lucide-react';

const App = () => {
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [analysis, setAnalysis] = useState([]);
  const [filterYear, setFilterYear] = useState('All');

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log("Fetching data...");
        const pRes = await axios.get('http://127.0.0.1:5000/api/prices');
        const eRes = await axios.get('http://127.0.0.1:5000/api/events');
        const aRes = await axios.get('http://127.0.0.1:5000/api/analysis');
        
        console.log("Prices received:", pRes.data.length);
        setPrices(pRes.data);
        setEvents(eRes.data);
        setAnalysis(aRes.data);
      } catch (err) {
        console.error("API Error:", err);
      }
    };
    fetchData();
  }, []);

  // Updated filter logic: ensure we are checking the date correctly
  const filteredData = prices.filter(p => {
    if (filterYear === 'All') return true;
    if (!p.Date) return false;
    // Check if the year string (e.g., "2014") exists in the date string (e.g., "Nov 24, 2014")
    return p.Date.toString().includes(filterYear);
  });

  return (
    <div style={{ backgroundColor: '#f8fafc', minHeight: '100vh', padding: '40px', fontFamily: 'sans-serif' }}>
      <header style={{ marginBottom: '40px', borderBottom: '2px solid #e2e8f0', paddingBottom: '20px' }}>
        <h1 style={{ color: '#1e293b', fontSize: '2.5rem', fontWeight: '800' }}>
          Birhan Energies <span style={{ color: '#3b82f6', fontWeight: '400' }}>| Market Intelligence</span>
        </h1>
        <p style={{ color: '#64748b' }}>Brent Oil Price Analysis & Change Point Detection</p>
      </header>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', marginBottom: '40px' }}>
        {analysis.map((item, idx) => (
          <div key={idx} style={{ background: 'white', padding: '20px', borderRadius: '12px', boxShadow: '0 4px 6px rgb(0 0 0 / 0.1)' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', color: '#3b82f6', marginBottom: '10px' }}>
              {idx === 0 ? <Calendar size={20}/> : <TrendingDown size={20}/>}
              <span style={{ fontWeight: '600', fontSize: '0.75rem' }}>{item.Metric}</span>
            </div>
            <div style={{ fontSize: '1.5rem', fontWeight: '700', color: '#1e293b' }}>{item.Value}</div>
          </div>
        ))}
      </div>

      <div style={{ background: 'white', padding: '20px', borderRadius: '12px', marginBottom: '20px', boxShadow: '0 1px 3px rgb(0 0 0 / 0.1)' }}>
        <label style={{ marginRight: '15px', fontWeight: '600' }}>Select Era:</label>
        <select onChange={(e) => setFilterYear(e.target.value)} style={{ padding: '8px', borderRadius: '6px' }}>
          <option value="All">Full History</option>
          <option value="2014">2014 OPEC Decision</option>
          <option value="2020">2020 COVID Shock</option>
          <option value="2022">2022 Ukraine War</option>
        </select>
      </div>

      <div style={{ background: 'white', padding: '30px', borderRadius: '16px', boxShadow: '0 10px 15px rgb(0 0 0 / 0.1)', marginBottom: '40px' }}>
        <h2 style={{ marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '10px' }}>
          <Activity color="#3b82f6" /> Price Visualization
        </h2>
        <div style={{ height: '400px', width: '100%' }}>
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={filteredData}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <XAxis dataKey="Date" tick={{fontSize: 10}} minTickGap={30} />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="Price" stroke="#3b82f6" strokeWidth={2} dot={false} />
              <ReferenceLine x="Nov 25, 2014" stroke="#ef4444" label="2014 Change Point" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div style={{ background: 'white', padding: '30px', borderRadius: '16px', boxShadow: '0 10px 15px rgb(0 0 0 / 0.1)' }}>
        <h2 style={{ marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '10px' }}>
          <AlertCircle color="#f59e0b" /> Historical Events Log
        </h2>
        <table style={{ width: '100%', textAlign: 'left', borderCollapse: 'collapse' }}>
          <thead>
            <tr style={{ borderBottom: '2px solid #f1f5f9', color: '#64748b' }}>
              <th style={{ padding: '12px' }}>Date</th>
              <th style={{ padding: '12px' }}>Event</th>
              <th style={{ padding: '12px' }}>Type</th>
            </tr>
          </thead>
          <tbody>
            {events.map((ev, i) => (
              <tr key={i} style={{ borderBottom: '1px solid #f1f5f9' }}>
                <td style={{ padding: '12px' }}>{ev.Date}</td>
                <td style={{ padding: '12px' }}>{ev.Event}</td>
                <td style={{ padding: '12px' }}>{ev.Type}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default App;