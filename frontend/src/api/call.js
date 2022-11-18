export default async function loginCall(username, password) {
    const response = await fetch("http://localhost.5000/user/login", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: username,
            password: password,
        }),
    })
    const result = response.json()
    if ((result["message"] = "True")) return true
    return false
}
