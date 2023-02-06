import { FormEventHandler } from 'react';
import { Form, FormGroup, Input, Button } from 'reactstrap';


interface Props {
    handleSubmit: FormEventHandler;
    handleFileChange: FormEventHandler
  }
  
  export const QRCodesForm: React.FC<Props> = ({ handleSubmit, handleFileChange }) => {
    return (
        <Form onSubmit={handleSubmit}>
            <FormGroup>
                <Input type="text" name="id_prefix" id="id_prefix" placeholder="prefix" />
            </FormGroup>
            <FormGroup>
                <Input type="text" name="id_suffix" id="id_suffix" placeholder="suffix" />
            </FormGroup>
            <FormGroup>
                <Input type="number" name="id_zeros" id="id_zeros" placeholder="zeros" />
            </FormGroup>
            <FormGroup>
                <Input type="number" name="amount" id="amount" placeholder="amount" required />
            </FormGroup>
            <FormGroup>
                <Input type="file" name="file" id="file" placeholder="Logo" onChange={handleFileChange} />
            </FormGroup>
            <Button color="primary" type="submit">Generate QR Codes</Button>
        </Form>
    )
  };