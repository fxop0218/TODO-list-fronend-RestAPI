import loginCall from "../api/call"
import { useForm } from "react-hook-form"
import React, { useState } from "react"
import TextField from "@material-ui/core/TextField"
import swal from "sweetalert"
import { SwipeableDrawer } from "@material-ui/core"

async function loginUser(credentials) {
    return fetch("http://localhost.5000/user/login", {
        method: "GET",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${process.env.REACT_APP_TOKEN}`,
        },
        async: true,
        body: JSON.stringify(credentials),
    }).then((data) => data.json())
}

function Login() {
    const [username, setUserName] = useState()
    const [password, setPassword] = useState()
    var user_loged = sessionStorage.getItem("user_loged")

    const handleSubmit = async (e) => {
        e.preventDefault()
        const response = await loginUser({ username, password })
        if ("accessToken" in response) {
            swal("Success", response.message, "success", { buttons: false, timer: 2000 }).then(
                (value) => {
                    localStorage.setItem("accessToken", response["accessToken"])
                    localStorage.setItem("user", JSON.stringify(response["user"]))
                }
            )
        } else {
            swal("Failed", response.message, "Error")
        }
    }

    return (
        <div className="flex h-screen justify-center items-center">
            {!user_loged ? (
                <form className="columns-1" noValidate onSubmit={handleSubmit}>
                    <div className="p-3">
                        <TextField
                            type="text"
                            name="username"
                            placeholder="Username"
                            onChange={(e) => setUserName(e.target.value)}
                        />
                    </div>

                    <div className="p-3">
                        <TextField
                            type="password"
                            name="password"
                            placeholder="Password"
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>
                    <div className="p-3 ">
                        <input
                            type="submit"
                            value="Submit"
                            className="bg-blue-700 w-20 rounded-md text-white content-center"
                        />
                    </div>
                </form>
            ) : (
                <p>Loged user</p>
            )}
        </div>
    )
}

export default Login
