import loginCall from "../api/call"

function Login() {
    var user_loged = sessionStorage.getItem("user_loged")
    const handleSubmit = async (event) => {
        event.preventDefault()
        var loged = await loginCall(
            event.target.elements.username.value,
            event.target.elements.password.value
        )
        if (loged.ok) this.setState({ isProcessing: false })
        console.log(`Hello: ${loged}`)
        alert(`Submitted form ${loged}`)
    }
    return (
        <div className="flex h-screen justify-center items-center">
            {!user_loged ? (
                <form className="columns-1" onSubmit={handleSubmit}>
                    <div className="p-3">
                        <input
                            type="text"
                            name="username"
                            placeholder="Username"
                            className="border-black text-center h-10"
                        />
                    </div>

                    <div className="p-3">
                        <input
                            type="password"
                            name="password"
                            placeholder="Password"
                            className="border-black text-center h-10"
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
