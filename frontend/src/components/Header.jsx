import { NavLink } from "react-router-dom"
import exit from "../scripts/scripts"

export const Header = () => {
    return (
        <>
            <header>
                <nav
                    className="flex flex-row justify-between bg-gray-100
                text-gray-500
                hover:text-gray-700
                focus:text-gray-700
                shadow-lg
                navbar navbar-expand-lg navbar-light"
                >
                    <div className="divide-y divide-dashed md:divide-solid">
                        <p className="text-blue-800 text-3xl font-bold p-5">App</p>
                    </div>
                    <div class="dropdown relative p-5">
                        <NavLink
                            to="/"
                            className="p-3"
                            activeClassName="active"
                            style={({ isActive }) => ({ color: isActive ? "blue" : "black" })}
                        >
                            Home
                        </NavLink>
                        <NavLink
                            to="/mainpage"
                            className="p-3"
                            activeClassName="active"
                            style={({ isActive }) => ({ color: isActive ? "blue" : "black" })}
                        >
                            Mainpage
                        </NavLink>
                        <NavLink
                            to="/Login"
                            className="p-3"
                            activeClassName="active"
                            style={({ isActive }) => ({ color: isActive ? "blue" : "black" })}
                        >
                            Login
                        </NavLink>
                        <button onClick={exit} className="text-black p-3 rounded bg-red-400">
                            Default
                        </button>
                    </div>
                </nav>
            </header>
        </>
    )
}
