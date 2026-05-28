import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<h1>Dashboard</h1>} />
        <Route path="/expenses" element={<h1>Expenses</h1>} />
        <Route path="/savings" element={<h1>Savings</h1>} />
        <Route path="/split-bills" element={<h1>Split Bills</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;