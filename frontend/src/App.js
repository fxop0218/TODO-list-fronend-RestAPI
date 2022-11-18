import { BrowserRouter as Router, Routes, Route, Redirect, BrowserRouter } from "react-router-dom"
import "./App.css"
import Home from "./pages/Home"
import Mainpage from "./pages/Mainpage"
import Login from "./pages/Login"
import { Header } from "./components/Header"

export default function App() {
    return (
        <div>
            <Header />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route index element={<Home />} />
                <Route path="/mainpage" element={<Mainpage />}></Route>
                <Route path="/login" element={<Login />}></Route>
            </Routes>
        </div>
    )
}
