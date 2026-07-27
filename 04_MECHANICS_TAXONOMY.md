# Mechanics Taxonomy

The taxonomy must remain layered.

## A. Elementary player actions

Select, move, swap, slide, push, pull, rotate, flip, place, remove, stack, unstack, merge, split, sort, group, separate, connect, disconnect, draw, cut, fold, stretch, compress, pour, redirect, lock, unlock, reveal, hide, activate, delay, grow, freeze, charge.

Classification is role-dependent: place a verb in this layer only when the player directly commands it. In 2048 the player commands a global directional `slide`; `merge` is instead automatic collision resolution. `Merge` remains an elementary action for games where the player explicitly selects objects to combine.

## B. Automatic system behaviours

Gravity, spawning, cascading, flow, diffusion, propagation, attraction, repulsion, collision, collision-triggered merging, pressure equalisation, growth, decay, ageing, state transformation, chain reaction, world rotation, opponent response, simultaneous resolution, delayed execution, random generation, deterministic generation.

## C. Constraints and scarce resources

Board space, moves, time, empty buffers, visibility, access order, capacity, energy, available actions, hand size, placement geometry, connectivity, sequence, synchronisation, irreversibility, probability, opponent pressure.

## D. Objectives and rewards

Clear board, reach target value, sort groups, form pattern, complete routes, maintain system, survive, maximise score, minimise moves, trigger cascade, balance quantities, reveal information, capture territory, deliver objects, reconstruct state.

## E. Information model

Perfect information, hidden information, random future information, previewed future information, partial observability, simultaneous unknown resolution.

## F. Time model

Static turn-based, turn-based with automatic resolution, real-time, real-time with pause, simultaneous planning and resolution, delayed actions across future turns.
