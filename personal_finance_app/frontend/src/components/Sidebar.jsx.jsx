import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="w-64 h-screen bg-white shadow-md p-6">

      {/* Logo */}
      <h1 className="text-2xl font-bold text-green-500 mb-10">
        StudlFinance
      </h1>

      {/* Navigation */}
      <nav className="flex flex-col gap-4">

        <Link
          to="/"
          className="bg-green-500 text-white px-4 py-3 rounded-xl"
        >
          Dashboard
        </Link>

        <Link
          to="/expenses"
          className="text-gray-700 hover:bg-gray-100 px-4 py-3 rounded-xl"
        >
          Expenses
        </Link>

        <Link
          to="/savings"
          className="text-gray-700 hover:bg-gray-100 px-4 py-3 rounded-xl"
        >
          Savings
        </Link>

        <Link
          to="/split-bills"
          className="text-gray-700 hover:bg-gray-100 px-4 py-3 rounded-xl"
        >
          Split Bills
        </Link>

      </nav>
    </div>
  );
}

export default Sidebar;
