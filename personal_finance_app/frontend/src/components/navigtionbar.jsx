import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="flex items-center justify-between px-6 py-4 bg-blue-600 text-white shadow-md">
      
      {/* App Name */}
      <div className="text-xl font-bold">
        StudlFinance
      </div>

      {/* Links */}
      <div className="flex gap-6 text-sm font-medium">
        <Link to="/" className="hover:text-gray-200">
          Dashboard
        </Link>

        <Link to="/expenses" className="hover:text-gray-200">
          Expenses
        </Link>

        <Link to="/savings" className="hover:text-gray-200">
          Savings
        </Link>

        <Link to="/split-bills" className="hover:text-gray-200">
          Split Bills
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;
