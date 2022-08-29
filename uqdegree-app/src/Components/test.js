import {useState, useEffect} from 'react';


function QueryCourses() {
    const [Courses, setCourses] = useState(0);

    useEffect(() => {
        // fetch('http://127.0.0.1:5000/courses').then(res => res.json()).then(data => {
        //   setCourses(data.courses); 
        // });
        fetch('http://127.0.0.1:5000/courses')
          .then((response) => response.json())
          .then((data) => setCourses(data));
      });

    var list = []

    list.push({title:'', id:0})
    for (const [i, value] of Courses.entries()) {
        list.push({title:value, id:i})
    }
    setCourses(list)
}

export default QueryCourses;
