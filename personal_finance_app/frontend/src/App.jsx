import Sidebar from "./components/Sidebar";

function App() {
  return (
    <div className="flex">
      <Sidebar />

      <div className="flex-1 p-6">
        <h1>App is working</h1>
      </div>
    </div>
  );
}

export default App;