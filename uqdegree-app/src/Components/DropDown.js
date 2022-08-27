import { Update } from "./Update";

function DropDown({courses}){
  
  var current = '';

  function Update(course) {
    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(course)
    };
    fetch('http://127.0.0.1:5000', requestOptions)
        .then(response => response.json());
    }  

  const getComboA = event => {
        // need to get the current value of select
        console.log(current) 
        Update([current, event.target.value])
        current = event.target.value
      }

    const listItems = courses.map(product =>
        <option key={product.id}>
          {product.title}
        </option>
      );

    return(
        <div>
            <select onChange={getComboA}>{listItems}</select>
        </div>
    )

}
export default DropDown;