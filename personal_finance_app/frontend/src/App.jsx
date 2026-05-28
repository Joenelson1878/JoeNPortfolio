import { BrowserRouter, Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";

function App() {
  return (
    <BrowserRouter>

      <div className="flex bg-gray-100 min-h-screen">

        <Sidebar />

        <div className="flex-1 p-8">

          <Routes>
            <Route path="/" element={<h1>Dashboard</h1>} />
            <Route path="/expenses" element={<h1>Expenses</h1>} />
            <Route path="/savings" element={<h1>Savings</h1>} />
            <Route path="/split-bills" element={<h1>Split Bills</h1>} />
          </Routes>

        </div>

      </div>

    </BrowserRouter>
  );
}

export default App;