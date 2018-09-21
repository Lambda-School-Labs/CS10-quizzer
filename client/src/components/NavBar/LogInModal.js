import React, { Component } from 'react'
import gql from 'graphql-tag'
import { Button, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap'
import PropTypes from 'prop-types'
import { Mutation } from 'react-apollo'
import './NavBar.css'

const userLoginQueryMutation = gql`
  mutation LoginUser($TeacherEmail: String!, $TeacherPW: String!) {
    queryTeacher(TeacherEmail: $TeacherEmail, TeacherPW: $TeacherPW) {
      teacher {
        TeacherEmail
      }
      jwtString
    }
  }`

class LogInModal extends Component {
  constructor () {
    super()
    this.state = {
      email: '',
      password: ''
    }
  }

  handleInputChange = event => {
    this.setState({ [event.target.name]: event.target.value })
  }

  render () {
    const { email, password } = this.state
    return (
      <Modal className='signup_login_modal' isOpen={this.props.logInModal} toggle={this.props.toggleLogIn}>
        <ModalHeader className='signup_login_modal_header'>
          <span>Log in</span>
        </ModalHeader>
        <ModalBody className='signup_login_modal_body'>
          <Mutation mutation={userLoginQueryMutation}>
            {(loginUser, { loading, error, data }) => (
              <div>
                <form onSubmit={event => {
                  event.preventDefault()
                  loginUser({ variables: { TeacherEmail: email, TeacherPW: password } })
                  this.setState({
                    email: '',
                    password: ''
                  })
                }}>
                  <div className='modal_div'>
                    <span>EMAIL</span>
                    <input type='email' name='email' value={email} onChange={this.handleInputChange} required />
                  </div>
                  <div className='modal_div'>
                    <span>PASSWORD</span>
                    <input type='password' name='password' value={password} onChange={this.handleInputChange} required />
                  </div>
                  <div className='modal_div'>
                    <Button type='submit' color='info' className='signup_login_modal_button'>Log in</Button>
                  </div>
                </form>
                {loading && <p>Signing you in...</p>}
                {(data || error) && this.props.attemptLogIn(data, error)}
              </div>
            )}
          </Mutation>
        </ModalBody>
        <ModalFooter className='signup_login_modal_footer'>
          <span className='modal_text'>Remember to log out on shared devices. <span>Forgot password?</span></span>
        </ModalFooter>
      </Modal>
    )
  }
}

LogInModal.propTypes = {
  logInModal: PropTypes.bool,
  toggleLogIn: PropTypes.func,
  attemptLogIn: PropTypes.func
}

export default LogInModal