"""Example pipeline implementation."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class PipelineContext:
    """Shared state between pipeline steps."""

    is_valid: bool = True


class PipelineStep(ABC):
    """Base class for all pipeline steps."""

    def __init__(self, context: PipelineContext) -> None:
        self.context = context

    @property
    def is_active(self) -> bool:
        """Whether this step should be executed."""
        return True

    @abstractmethod
    def handle(self) -> None:
        """Execute step logic."""
        raise NotImplementedError


class IsValidCheckerStep(PipelineStep):
    """Example pipeline step."""

    @property
    def is_active(self) -> bool:
        return self.context.is_valid

    def handle(self) -> None:
        """Execute step logic."""
        print("Executing validation step...")


class Pipeline:
    """Pipeline executor."""

    steps = (
        IsValidCheckerStep,
    )

    def execute(self, context: PipelineContext) -> None:
        for step_class in self.steps:
            step = step_class(context)
            if step.is_active:
                step.handle()
