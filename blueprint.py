from source import Grid


def slice_grid(
    grid: Grid, topleft: tuple[int, int], bottomright: tuple[int, int]
) -> Grid:
    """Return a 2D slice of the given 2D-array from topleft to bottomright
    inclusive of both corners.

    Example:
    >>> slice_grid([[0, 1, 0], [0, 0, 1], [1, 1, 1]], (0, 0), (1, 2))
    [[0, 1], [0, 0], [1, 1]]
    """
    ...


class Blueprint:
    """Blueprint class for storing a blueprint of a rectangular GoL pattern."""

    def __init__(self, grid: Grid):
        self.grid = grid

    def __repr__(self) -> str:
        """Return a string representation of the blueprint."""
        ...

    def __eq__(self, other: "Blueprint") -> bool:
        """Return True if the two blueprints are equal, False otherwise."""
        ...

    @classmethod
    def from_grid(
        cls, full_grid: Grid, topleft: tuple[int, int], bottomright: tuple[int, int]
    ) -> "Blueprint":
        """Create a blueprint from a subgrid of a full grid."""
        blueprint_grid: Grid = ...
        return cls(blueprint_grid)

    def serialize(self) -> str:
        """Return a string from which the blueprint can be reconstructed."""
        ...

    @classmethod
    def deserialize(cls, str_repr: str) -> "Blueprint":
        """Return a blueprint from a serialized string.
        
        serialize and deserialize should be inverses of each other, i.e.: 
        >>> bp == Blueprint.deserialize(bp.serialize())
        """
        grid: Grid = ...  # get a Grid object from str_repr
        return cls(grid)

    def get_rotated(self) -> "Blueprint":
        """Return a new blueprint that is rotated 90 degrees clockwise."""
        ...

    def get_flipped(self) -> "Blueprint":
        """Return a new blueprint that is flipped horizontally."""
        ...

    def get_reverted(self) -> "Blueprint":
        """Return a new blueprint that is a negative of the original.
        That is, all live cells are dead and all dead cells are alive.
        """
        ...
