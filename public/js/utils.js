// URL global del backend
const API_URL = "https://s3b4.pythonanywhere.com/mascotas";

const postData = async (url = API_URL, data) => {
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const raw = JSON.stringify(data);
    const requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    return await fetch(url, requestOptions)
}

const getDataById = async (url = API_URL, id) => {
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
    }

    const response = await fetch(`${url}/${id}`, requestOptions)
    const data = await response.json()
    return data
}

const updateData = async (url = API_URL, id, data) => {
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const raw = JSON.stringify(data);
    const requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };
    const response = await fetch(`${url}/${id}`, requestOptions)
    return await response.json()
}

const deleteData = async (url = API_URL, id) => {
    let myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const requestOptions = {
        method: 'DELETE',
        headers: myHeaders,
        redirect: 'follow'
    };
    return await fetch(`${url}/${id}`, requestOptions)
}

export { postData, getDataById, updateData, deleteData }
