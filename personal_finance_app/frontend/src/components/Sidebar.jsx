import "/Users/joenelson/Desktop/JoeNPortfolio/personal_finance_app/frontend/src/components/Sidebar.css";

function Sidebar() {
  return (
    <nav className="sidebar">
      <div className="nav-logo">
        <strong>StudlyFinance</strong>
      </div>

      <div className="nav-links">
        <a href="/">Dashboard</a>
        <a href="/expenses">Expenses</a>
        <a href="/savings">Savings</a>
        <a href="split bills">Split Bills</a>
      </div>

      <div className="nav-auth">
        <a href="/login">Log In</a>
        <a href="/register">Register</a>
      </div>
    </nav>
  );
}

export default Sidebar;

