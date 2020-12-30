import React from "react";
import { uid } from "react-uid";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";

import Student from "./../Student";

import "./styles.css";

/* Component for the List of Students */
class StudentList extends React.Component {
  render() {
    const { students, queueComponent } = this.props;

    /* Our student list.  We use the state to iterate through the 
       student list and make an <li> for each one. */
    return (
      <Table className="student-list">
        <TableBody>
          {students.map(student => (
            <Student
              key={uid(
                student
              )} /* unique id required to help React render more efficiently when we modify the students list. */
              student={student}
              queueComponent={queueComponent}
            />
          ))}
        </TableBody>
      </Table>
    );
  }
}

export default StudentList;
