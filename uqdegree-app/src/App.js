import './App.css';
import Table from './Components/Table';
import {useState, useEffect} from 'react';
import { useBetween } from "use-between"

function App() {
  //const [Courses, setCourses] = useState([]);

  const useFormState = () => {
    const [Courses, setCourses] = useState([]);
    return {
      Courses, setCourses
    };
  };

  const useSharedFormState = () => useBetween(useFormState);

  const {Courses, setCourses} = useSharedFormState();

    function DataToObject(courseList) {
      var list = []
      list.push({title:'', id:0})
      for (const [i, value] of courseList.entries()) {
          list.push({title:value, id:i+1})
      }
      return list
    }

    function QueryCourses(){
      // useEffect(() => {
        fetch('http://127.0.0.1:5000/courses')
          .then((response) => response.json())
          .then((data) => setCourses(DataToObject(data)));
      // }, []);
      // console.log(Courses)
      // var list = []
    }

      // list.push({title:'', id:0})
      // for (const [i, value] of Courses.entries()) {
      //     list.push({title:value, id:i})
      // }
      // setCourses(list)
      // console.log(Courses)
    //  QueryCourses()
  // const list = [
  //   { title: '', id: 0 },
  //   { title: 'COSC3500', id: 1 },
  //   { title: 'MATH1071', id: 2 },
  //   { title: 'ECON1010', id: 3 },
  // ];

  useEffect(() => {
    // const list = [
    //   { title: '', id: 0 },
    //   { title: 'COSC3500', id: 1 },
    //   { title: 'MATH1071', id: 2 },
    //   { title: 'ECON1010', id: 3 },
    // ];
    // setCourses(list);
    QueryCourses();
  }, [])

  // setCourses(list);

  return (
    <div className="App">
      <Table useShared={useSharedFormState} />
    </div>
  );
}

export default App;
