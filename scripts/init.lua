-- Build: b597dbeb8fec8b190b6b426ff52a3838
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
