function Update({course}) {
    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({course})
    };
    console.log({course})
    fetch('http://127.0.0.1:5000', requestOptions)
        .then(response => response.json());
    }
export { Update };