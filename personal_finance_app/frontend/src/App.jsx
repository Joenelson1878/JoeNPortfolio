import { Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import Expenses from "./pages/Expenses";
import Savings from "./pages/Savings";
import SplitBills from "./pages/SplitBills";

function App() {
  return (
    <div className="flex">
      {/* Sidebar stays always visible */}
      <Sidebar />

      {/* Page content changes here */}
      <div className="flex-1 p-6 bg-gray-50 min-h-screen">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/expenses" element={<Expenses />} />
          <Route path="/savings" element={<Savings />} />
          <Route path="/split-bills" element={<SplitBills />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;