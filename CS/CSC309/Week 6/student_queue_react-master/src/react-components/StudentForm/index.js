import React from "react";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";

import Input from "./../Input";

import "./styles.css";

/* Component for the Student Form */
class StudentForm extends React.Component {
  render() {
    const {
      studentName,
      handleChange,
      studentCourse,
      position,
      addStudent
    } = this.props;

    return (
      <Grid className="student-form" container spacing={4}>
        {/* Inputs to add student */}
        <Input
          name="studentName"
          value={studentName}
          onChange={handleChange}
          label="Student"
        />

        <Input
          name="studentCourse"
          value={studentCourse}
          onChange={handleChange}
          label="Course"
        />

        <Input
          name="position"
          value={position}
          onChange={handleChange}
          label="Add at Position"
        />

        <Grid
          className="student-form__button-grid"
          item
          xl={2}
          lg={2}
          md={12}
          s={12}
          xs={12}
        >
          <Button
            variant="contained"
            color="primary"
            onClick={addStudent}
            className="student-form__submit-button"
          >
            Add Student
          </Button>
        </Grid>
      </Grid>
    );
  }
}

export default StudentForm;
