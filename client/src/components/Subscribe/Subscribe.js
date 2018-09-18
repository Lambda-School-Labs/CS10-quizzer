import React, { Component } from 'react';
import { CardElement, injectStripe } from 'react-stripe-elements';

class Subscribe extends Component {
    constructor(props) {
        super(props);
        this.submit = this.submit.bind(this);
    }

    async submit(e) {

    }

    render() {
        return (
            <div>
                <p>Would you like to complete the purchase?</p>
                <CardElement />
                <button onClick={ this.submit }> Send </button>
            </div>
        );
    }
}

export default injectStripe(Subscribe);