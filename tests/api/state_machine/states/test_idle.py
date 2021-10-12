import pytest

from isar.models.mission import Mission
from isar.state_machine.state_machine import StateMachine
from models.enums.states import States
from models.planning.step import DriveToPose
from tests.test_utilities.mock_models.mock_robot_variables import mock_pose


@pytest.mark.parametrize(
    "mock_should_start_mission, next_expected_state",
    [
        (
            (
                True,
                Mission([DriveToPose(pose=mock_pose())]),
            ),
            States.Send,
        ),
        ((False, None), States.Idle),
    ],
)
def test_idle_iterate(
    idle_state,
    mocker,
    mock_should_start_mission,
    next_expected_state,
):
    mocker.patch.object(
        StateMachine, "should_start_mission", return_value=mock_should_start_mission
    )
    next_state: States = idle_state.get_next_state()
    assert next_state == next_expected_state