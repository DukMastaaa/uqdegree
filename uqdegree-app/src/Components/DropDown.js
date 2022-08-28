import {useState, useEffect} from 'react';

function DropDown({useShared}) {

  var current = '';

  const {Courses, setCourses} = useShared();

  // function DataToObject(courseList) {
  //   var list = []
  //   list.push({title:'', id:0})
  //   for (const [i, value] of courseList.entries()) {
  //       list.push({title:value, id:i+1})
  //   }
  //   console.log(list)
  //   return list
  // }

  // function QueryCourses(){
  //   // useEffect(() => {
  //     // fetch('http://127.0.0.1:5000/courses').then(res => res.json()).then(data => {
  //     //   setCourses(data.courses); 
  //     // });
  //     fetch('http://127.0.0.1:5000/courses')
  //       .then((response) => response.json())
  //       .then( (data) => 
  //       useEffect(() => { setCourses(DataToObject(data))
  //           }, [Courses])
  //         );
      
  //       // }, []);
  // }

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
        // console.log(current) 
        Update([current, event.target.value])
        current = event.target.value
       // QueryCourses()
        // console.log(Courses)
      }

    var listItems
  

    const list = [
        { title: '', id: 0 },
        { title: 'COSC3500', id: 1 },
        { title: 'MATH1071', id: 2 },
        { title: 'ECON1010', id: 3 },
      ];
    // useEffect(() => {
      // console.log(Courses);
      listItems = Courses.map(list =>
        <option key={list.id}>
          {list.title}
        </option>
      );
    // }, [Courses])

  return(
      <div>
          <select onClick={getComboA}>{listItems}</select>
      </div>
  )

}
export default DropDown;