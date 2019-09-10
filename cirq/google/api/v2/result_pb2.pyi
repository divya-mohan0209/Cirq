# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import cirq.google.api.v2.program_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing

class Result(google.protobuf.message.Message):

    @property
    def sweep_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[SweepResult]: ...

    def __init__(self,
        sweep_results : typing.Optional[typing.Iterable[SweepResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Result: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class SweepResult(google.protobuf.message.Message):
    repetitions = ... # type: int

    @property
    def parameterized_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[ParameterizedResult]: ...

    def __init__(self,
        repetitions : typing.Optional[int] = None,
        parameterized_results : typing.Optional[typing.Iterable[ParameterizedResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> SweepResult: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class ParameterizedResult(google.protobuf.message.Message):

    @property
    def params(self) -> ParameterDict: ...

    @property
    def measurement_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[MeasurementResult]: ...

    def __init__(self,
        params : typing.Optional[ParameterDict] = None,
        measurement_results : typing.Optional[typing.Iterable[MeasurementResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ParameterizedResult: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class MeasurementResult(google.protobuf.message.Message):
    key = ... # type: typing.Text

    @property
    def qubit_measurement_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[QubitMeasurementResult]: ...

    def __init__(self,
        key : typing.Optional[typing.Text] = None,
        qubit_measurement_results : typing.Optional[typing.Iterable[QubitMeasurementResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MeasurementResult: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class QubitMeasurementResult(google.protobuf.message.Message):
    results = ... # type: bytes

    @property
    def qubit(self) -> cirq.google.api.v2.program_pb2.Qubit: ...

    def __init__(self,
        qubit : typing.Optional[cirq.google.api.v2.program_pb2.Qubit] = None,
        results : typing.Optional[bytes] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> QubitMeasurementResult: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...

class ParameterDict(google.protobuf.message.Message):
    class AssignmentsEntry(google.protobuf.message.Message):
        key = ... # type: typing.Text
        value = ... # type: float

        def __init__(self,
            key : typing.Optional[typing.Text] = None,
            value : typing.Optional[float] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ParameterDict.AssignmentsEntry: ...
        def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
        def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...


    @property
    def assignments(self) -> typing.MutableMapping[typing.Text, float]: ...

    def __init__(self,
        assignments : typing.Optional[typing.Mapping[typing.Text, float]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ParameterDict: ...
    def MergeFrom(self, other_msg: google.protobuf.message.Message) -> None: ...
    def CopyFrom(self, other_msg: google.protobuf.message.Message) -> None: ...