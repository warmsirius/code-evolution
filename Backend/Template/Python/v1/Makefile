.PHONY: docs livehtml html clean open build
docs:
	$(MAKE) -C docs html
live-docs:
	$(MAKE) -C docs livehtml
clean-docs:
	$(MAKE) -C docs clean
open-docs:
	$(MAKE) -C docs open
build-docs: 
	$(MAKE) -C docs build

.PHONY: format lint type
# 格式检查
format:
	ruff format .

# 代码检查(包含自动修复)
lint:
	ruff check --fix .

# 类型检查
type:
	mypy .

# 完整检查
check: format lint type

# 清理
clean:
	ruff clean
	rm -rf .mypy_cache .ruff_cache