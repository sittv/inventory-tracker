const base_url = "http://localhost:5000/api";

export async function check_login(password) {
    return fetch(`${base_url}/check_login`, {
        method: "POST",
        body: JSON.stringify({password}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    }).then(value => {
        return value.status === "good";
    }).catch(reason => {
        console.error(reason);
        return false;
    })
}


export async function add_user(current_login, name, password) {
    return fetch(`${base_url}/add_user`, {
        method: "POST",
        body: JSON.stringify({current_login, name, password}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    })
}


export async function get_items() {
    return fetch(`${base_url}/get_items`, {
        method: "GET",
    }).then(v => {
        return v.json()
    })
}


export async function add_item(current_login, name, location, barcode) {
    return fetch(`${base_url}/add_item`, {
        method: "POST",
        body: JSON.stringify({current_login, name, location, barcode}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    })
}

export async function set_barcode(current_login, barcode, item_id) {
    return fetch(`${base_url}/add_item`, {
        method: "POST",
        body: JSON.stringify({current_login, barcode, item_id}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    })
}


export async function id_checkout(current_login, item_id) {
    return fetch(`${base_url}/id_checkout`, {
        method: "POST",
        body: JSON.stringify({current_login, item_id}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    })
}

export async function id_return(current_login, item_id) {
    return fetch(`${base_url}/id_return`, {
        method: "POST",
        body: JSON.stringify({current_login, item_id}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    })
}


export async function barcode_checkout(current_login, barcode) {
    return fetch(`${base_url}/id_return`, {
        method: "POST",
        body: JSON.stringify({current_login, barcode}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    })
}

export async function barcode_return(current_login, barcode) {
    return fetch(`${base_url}/id_return`, {
        method: "POST",
        body: JSON.stringify({current_login, barcode}),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(v => {
        return v.json()
    })
}

