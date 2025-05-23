import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { DragDropList } from './components/DragDropList';

const Home: React.FC = () => (
  <div style={{ padding: '20px' }}>
    <h2>Добро пожаловать в интернет-магазин!</h2>
    <p>Это демонстрационный интерфейс.</p>
  </div>
);

const DndPage: React.FC = () => (
  <div style={{ padding: '20px' }}>
    <h2>Управление товарами</h2>
    <DragDropList />
  </div>
);

export const App: React.FC = () => {
  return (
    <Router>
      <nav style={{ padding: '10px', background: '#eee' }}>
        <Link to="/" style={{ marginRight: '10px' }}>Главная</Link>
        <Link to="/dnd">Управление товарами</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dnd" element={<DndPage />} />
      </Routes>
    </Router>
  );
};
