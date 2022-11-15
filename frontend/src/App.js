import { BrowserRouter as Router, Routes, Route, Redirect, BrowserRouter } from "react-router-dom"
import "./App.css"
import Home from "./pages/Home"
import Mainpage from "./pages/Mainpage"
import { Header } from "./components/Header"

export default function App() {
    return (
        <div>
            <Header />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route index element={<Home />} />
                <Route path="/mainpage" element={<Mainpage />}></Route>
            </Routes>
        </div>
    )
}
