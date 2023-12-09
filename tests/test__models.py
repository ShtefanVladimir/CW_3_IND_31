def test_convert_payment(operation_instances):
    operation = operation_instances[0]
    assert operation.convert_payment("Maestro 1596837868705199") == "XXXX XX** **** XXXX"
